<template>
  <h2>作业提交</h2>
  <div class="homework">
    <h3>提交zip</h3>
    <UpLoad file-type="zip"></UpLoad>
    <h3>提交pdf</h3>
    <UpLoad file-type="pdf"></UpLoad>
    <h3>提交mp4</h3>
    <UpLoad file-type="mp4"></UpLoad>
    <h3>提交txt</h3>
    <UpLoad file-type="txt"></UpLoad>
  </div>
</template>

<script>
import UpLoad from "@/components/UpLoad";

export default {
  name: "Student",
  components: {
    UpLoad
  }
}
</script>

<style scoped>
.homework{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
