<template>

  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">

    <router-link class="navbar-brand text-style" to="/">作业提交系统</router-link>

    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item mx-3">
          <router-link class="btn btn-primary" aria-current="page" to="/">主页</router-link>
        </li>
        <li class="nav-item mx-2">
          <router-link class="btn btn-success" to="/student">学生上传</router-link>
        </li>
        <li class="nav-item">
          <router-link class="btn btn-success" to="/teacher">老师下载</router-link>
        </li>

      </ul>
    </div>
  </div>
</nav>
</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style scoped>
.text-style{
  font-size:  30px !important;
  font-family: fantasy !important;
  color: brown !important;
}
</style>
