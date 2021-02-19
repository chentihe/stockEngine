<template>
  <div class="home container">
    <div class="my-4">
      <div class="form text-center">
        <form @submit.prevent="onSubmit">
          <label class="form-label"><strong>Search for Stock Info</strong></label>
          <div class="input-group mb-3">
            <input 
                v-model="stock_no" 
                class="form-control"
                placeholder="Type The Stock No">
            <button type="submit" 
                    class="btn btn-sm btn-outline-secondary">
                    Submit
            </button>
          </div>
        </form>
      </div>
    <div 
      class="news text-center "
      v-if="stock_no"
      >
      <table class="table table-striped">
      <thead>
          <tr>
            <th>新聞名稱</th>
            <th>發布日期</th>
            <th>來源網站</th>
          </tr>
      </thead>
      <tbody>
        <NewsComponent
          v-for="news in newses"
          :news="news"
          :key="news.stock_no"
        />
      </tbody>
      </table>
    </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "@/common/api.service.js";
import NewsComponent from "@/components/News.vue";

export default {
  name: "Home",
  components:{
    NewsComponent,
  },
  data() {
      return {
        stock_no: null,
        newses: [],
        error: null
      }
  },
  methods: {
    onSubmit() {
        if (!this.stock_no) {
            this.error = "Please send a stock no!"
        } else {
            let endpoint = `/api/news/${this.stock_no}/`;
            apiService(endpoint)
                .then(data => {
                  this.newses = data;
                })
    }
    }
  },
  created() {
    document.title = "Stock News"
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