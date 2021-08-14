<template>
  <input class="file" name="file" type="file" accept="image/png,image/gif,image/jpeg" @change="upload"/>
</template>

<script>
export default {
  name: 'UpLoad',
  methods: {
    upload(e){
      let file = e.target.files[0];
      let form = new FormData();
      form.append('file', file);
      console.log(form.get('file'));
      this.$http.post('http://127.0.0.1:5000/upload', form,
          {headers:{'Content-Type':'application/x-www-form-urlencoded'}})
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.log(error);
      });
    }
  }
}
</script>

<style scoped>

</style>
