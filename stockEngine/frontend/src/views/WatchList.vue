<template>
  <div class="watchlist container">
    <div
      class="watchlist text-center">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>              
              <button
                class="btn btn-sm btn-outline-danger"
                @click="deleteStock">
                Delete
              </button>
            </th>
            <th>股票代號</th>
            <th>股票名稱</th>
          </tr>
        </thead>
        <tbody>
            <tr
              v-for="(watchList, index) in getLists"
              :watchList="watchList"
              :key="index"
              >
              <td>
                <input type="checkbox" 
                      class="form-check-input"
                      :value="watchList"
                      v-model="selectedStocks">
              </td>
              <td>
                <router-link 
                  :to="{ name: 'StockNews', params: { stockNo: watchList.stock_no } }">
                  {{ watchList.stock_no }}
                </router-link>
              </td>
              <td>{{ watchList.stock_name }}</td>
            </tr>
        </tbody>
      </table>
    </div>
    <div class="my-4">
      <p v-if="!haveWatchList">
        You Don't Have Any Stock within WatchList
      </p>
      <Pagination
        v-if="haveWatchList"
        :paginationService="pagination"
        v-on:pageService="getWatchList"
      />
    </div>
  </div>

</template>

<script>
import { apiService } from "@/common/api.service.js";
import Pagination from "@/components/Pagination.vue";

export default {
    name: "WatchList",
    components: {
      Pagination
    },
    data() {
        return {
            getLists: [],
            selectedStocks: [],
            haveWatchList: false,
            pagination: {}
        }
    },
    methods: {
      // 接收用戶的觀察清單
      getWatchList(page = 1) {
        let endpoint = `api/watchlist/?page=${page}`;
          apiService(endpoint)
            .then(data => {
              if(data.results.length > 0) {
                this.haveWatchList = true;
                this.getLists = [];
                this.getLists.push(...data.results);
                this.pagination = data.pagination;
              } else {
                this.haveWatchList = false;
              }
            })
      },
      // 用戶將該股移除觀察清單(可批次刪除)
      async deleteStock() {
        if (this.selectedStocks.length > 0) {
          for (var i = 0; i < this.selectedStocks.length; i++){
            let endpoint = `api/watchlist/${this.selectedStocks[i].stock_no}/`;
            await apiService(endpoint, "DELETE");
            const index = this.getLists.indexOf(this.selectedStocks[i]);
            this.getLists.splice(index, 1);
          };
          this.getWatchList();
          this.selectedStocks = [];
      }}
    },
    created() {
      document.title = "Watch List";
      this.getWatchList();
    }
}
</script>

<style scoped>
  .table {
    color: dimgrey;
  }
  a {
      text-decoration: none;
      color: dimgrey;
  }
  a:hover {
      color: teal;
  }
</style>