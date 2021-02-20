<template>
    <tr>
        <td>
            <a :href="news.link">{{ news.title }}</a>
        </td>
        <td>{{ news.published_at }}</td>
        <td><img :src="news.source" style="width:32px; heigh:32px;" /></td>
    </tr>
</template>

<script>
export default {
    name: "NewsComponent",
    props:{
        news: {
            type: Object,
            required: true
        }
    }
}
</script>

<style scoped>
a {
    text-decoration:none;
    color:lightsteelblue;
}
a:hover {
    color:teal;
}
</style>