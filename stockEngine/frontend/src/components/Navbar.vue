<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link
        :to="{ name: 'Home' }"
        class="navbar-brand"
        >stockEngine
      </router-link>

      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <router-link
                  :to="{ name: 'Home' }"
                  class="btn btn-sm btn-success"
              >Home
            </router-link>
          </li>
          <li class="nav-item">
            <a class="btn btn-sm btn-outline-secondary" href="/accounts/logout/"
              >Logout
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
    name: "NavbarComponent"
}
</script>

<style>
    .my-navbar {
        border-bottom: 1px solid #DDD;
    }

    .navbar-brand {
        font-weight: bold;
        font-size: 130%;
    }
    .navbar-brand:hover {
        color: #C0C0C0 !important;
    }
</style>