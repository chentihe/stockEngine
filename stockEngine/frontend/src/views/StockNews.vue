<template>
  <div class="stocknews container">
    <div class="my-4">
    <div class="btn-group" 
        role="group">
      <button type="button" 
              class="btn btn-warning">
        <strong>
          {{ stockData.stock_no }}
        </strong>
      </button>
      <button type="button" 
              class="btn btn-warning">
        <strong>
          {{ stockData.stock_name }}
        </strong>
      </button>
      <button type="button" 
              class="btn btn-warning"
              @click="toggleLike">
        <i class="fas fa-bookmark"
          v-if="addWL"></i>
        <i class="far fa-bookmark"
          v-else></i>
      </button>
    </div>
    <div 
      class="news text-center mt-1"
      >
      <NewsComponent
        :newsList="newses"
      />
      <div class="my-4">
        <p v-if="!getNews">
          No News for the Stock: {{ this.stockData.stock_name }}
        </p>
        <Pagination
          v-if="getNews"
          :paginationService="pagination"
          v-on:pageService="sendNewsReq"
        />
      </div>
    </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "@/common/api.service.js";
import NewsComponent from "@/components/News.vue";
import Pagination from "@/components/Pagination.vue";

export default {
  name: "StockNews",
  components:{
    NewsComponent,
    Pagination
  },
  props: {
    stockNo: {
      type: String,
      required: true
    }
  },
  data() {
      return {
        stockData: {},
        getStock: [],
        newses: [],
        addWL: false,
        pagination: {},
        getNews: false,
      }
  },
  methods: {
    // 接收該股相關的新聞
    sendNewsReq(page = 1) {
      let endpoint = `/api/news/${this.stockNo}/?page=${page}`;
      apiService(endpoint)
        .then(data => {
          if (data.results.length > 0) {
            this.newses = []
            this.newses.push(...data.results)
            this.pagination = data.pagination
            this.getNews = true
          } else {
            this.getNews = false
          }
        })
    },
    // 接收該股的股票代號與公司名稱
    sendStockReq() {
      let endpoint = `/api/stock/${this.stockNo}/`;
        apiService(endpoint)
            .then(data => {
              this.stockData = data
            });
    },
    // 加入觀察清單按鈕
    toggleLike() {
      this.addWL === false
        ? this.addtoWL()
        : this.rmfromWL()
    },
    // 加入該股到觀察清單
    addtoWL() {
      let endpoint = `api/watchlist/`;
        apiService(endpoint, "POST", { stock_no: this.stockNo })
      this.addWL = true;
    },
    // 從觀察清單移除該股
    rmfromWL() {
      let endpoint = `/api/watchlist/${this.stockData.stock_no}/`;
        apiService(endpoint, "DELETE")
      this.addWL = false;
    },
    // 檢查該股是否有在觀察清單中
    searchStock() {
      this.addWL = false;
      let endpoint = `/api/watchlist/?search=${this.stockNo}`
      apiService(endpoint)
        .then(data => {
          if (data.results.length > 0) {
            this.getStock = data.results[0]
            this.addWL = true
          } else {
            this.getStock = []
          };
        })
      },
  },
  created() {
    document.title = "Stock News"
    this.sendStockReq()
    this.sendNewsReq()
    this.searchStock()
  },
};
</script>

<style scoped>
  input.form-control:focus{
    border-color:#ccc;
    outline: none;
    box-shadow: none;
  }
</style>