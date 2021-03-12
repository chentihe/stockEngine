import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import WatchList from "../views/WatchList.vue";
import StockNews from "../views/StockNews.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    props: true,
  },
  {
    path: "/watchlist",
    name: "WatchList",
    component: WatchList
  },
  {
    path: "/stocknews/:stockNo",
    name: "StockNews",
    component: StockNews,
    props: true,
  }
];

const router = new VueRouter({
  mode: "history",
//  base: process.env.BASE_URL,
  routes
});

export default router;
