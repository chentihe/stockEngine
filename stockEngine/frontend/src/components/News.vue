<template>
  <table class="table table-striped">
    <thead>
      <tr>
        <th>新聞名稱</th>
        <th>發布日期</th>
        <th>來源網站</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(news, index) in newsList"
          :news="news"
          :key="index">
        <td>
            <a :href="news.link"
            >{{ news.title }}</a>
        </td>
        <td>{{ news.published_at }}</td>
        <td><img :src="news.source" style="width:32px; heigh:32px;" /></td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
    name: "NewsComponent",
    props: {
        newsList: {
            type: Array,
            required: true
        }
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