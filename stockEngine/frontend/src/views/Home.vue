<template>
  <div class="home container">
    <div class="my-4">
      <div class="form text-center">
        <form @submit.prevent="onSubmit">
          <label class="form-label"><strong>Search for Stock Info</strong></label>
          <div class="input-group mb-3">
            <input 
                v-model="stockNo" 
                class="form-control"
                placeholder="Type The Stock No">
            <button type="submit" 
                    class="btn btn-sm btn-outline-secondary"
                    >Submit
            </button>
          </div>
        </form>
      </div>
    <div class="btn-group" 
        role="group"
        v-if="isShow">
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
      v-if="isShow"
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
    <div v-else>
      <p v-if="error" class="error mt-2"> {{ error }} </p>
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
  name: "Home",
  components:{
    NewsComponent,
    Pagination
  },
  data() {
      return {
        stockNo: null,
        newsUrl: null,
        stockData: {},
        getStock: [],
        error: null,
        isShow: false,
        getNews: false,
        addWL: false,
        loadingNews: false,
        newses: [],
        pagination: {}
      }
  },
  methods: {
    // 接收該股相關的新聞
    sendNewsReq(page = 1) {
      let endpoint = `${this.newsUrl}?page=${page}`;
      console.log(endpoint)
      this.loadingNews = true;
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
      let endpoint = this.stockAPI;
      console.log(endpoint);
        apiService(endpoint)
            .then(data => {
              if (data) {
                this.stockData = data
              } else {
                this.stockData = []
              }
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
        apiService(endpoint, "POST", { stock_no: this.stockData.stock_no });
      this.addWL = true;
    },
    // 從觀察清單移除該股
    rmfromWL() {
      let endpoint = `/api/watchlist/${this.stockData.stock_no}/`;
        apiService(endpoint, "DELETE");
      this.addWL = false;
    },
    // 檢查該股是否有在觀察清單中
    searchStock() {
      this.addWL = false;
      let endpoint = this.getStockAPI;
      console.log(endpoint);
      apiService(endpoint)
        .then(data => {
          if (data.results.length > 0) {
            this.getStock = data.results[0];
            this.addWL = true;
          } else {
            this.getStock = []
          };
        })
      },
    onSubmit() {
      if (this.stockNo) {
        this.newses = [];
        this.newsUrl = this.newsAPI;
        this.sendStockReq();
        this.sendNewsReq();
        this.searchStock();
        this.stockNo = "";
        this.isShow = true;
      } else {
        this.isShow = false;
        this.error = "Please enter a stock no!"
      }
    }
  },
  computed: {
    stockAPI: function() {
      return `/api/stock/${this.stockNo}/`
    },
    newsAPI: function() {
      return `/api/news/${this.stockNo}/`
    },
    getStockAPI: function() {
      return `/api/watchlist/?search=${this.stockNo}`
    }
  },
  created() {
    document.title = "Stock Engine"
  }
};
</script>

<style scoped>
  input.form-control:focus{
    border-color:#ccc;
    outline: none;
    box-shadow: none;
  }
</style>