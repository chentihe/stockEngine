<template>
    <nav aria-label="Page navigation">
        <ul class="pagination
                    justify-content-center">
            <li class="page-item"
                :class="{'disabled': !paginationService.previous}">
                <a class="page-link" 
                    href="#" 
                    aria-label="Previous"
                    @click.prevent="getPagesService(paginationService.current_page - 1)"
                    tabindex="-1">
                    <span aria-hidden="true">&laquo;</span>
                    <span class="sr-only">Previous</span>
                </a>
            </li>
            <li class="page-item"
                      v-for="pages in paginationService.total_pages"
                      :key='pages'
                      :class="{'active': paginationService.current_page === pages}">
                      <a class="page-link" 
                        href="#"
                        @click.prevent='getPagesService(pages)'
                      >{{ pages }}
                      </a>
            </li>
            <li class="page-item"
                :class="{'disabled': !paginationService.next}">
                <a class="page-link"
                  href="#"
                  aria-label="Next"
                  @click.prevent="getPagesService(paginationService.current_page + 1)">
                    <span aria-hidden="true">&raquo;</span>
                    <span class="sr-only">Next</span>
                </a>
            </li>
        </ul>
    </nav>
</template>

<script>
export default {
    name: "Pagination",
    props: {
        paginationService: {
            type: Object,
            required: true
        }
    },
    methods: {
      // 把用戶點擊的頁數傳到父元件做資料更新
      getPagesService(page) {
        this.$emit('pageService', page)
      }
    }
}
</script>

<style scoped>
  a {
      text-decoration: none;
      color: lightsteelblue;
  }
  a:hover {
      color: teal;
  }
  .pagination > .active > a {
      background-color: slategray !important;
      border: solid 1px slategray !important;
  }
</style>