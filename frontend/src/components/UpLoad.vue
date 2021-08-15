<template>
  <input class="file" name="file" type="file" :accept="accept" @change="upload"/>
</template>

<script>
export default {
  name: 'UpLoad',
  props: {
    fileType: {
      type: String,
      default: "anyType"
    }
  },
  data() {
    return {
      accept: ""
    }
  },
  created: function () {
    this.accept = ".".concat(this.fileType)
  },
  methods: {
    upload(e){
      let file = e.target.files[0];
      let form = new FormData();
      form.append('file', file);
      console.log(form.get('file'));
      let url = 'http://127.0.0.1:5000/upload';
      url = url.concat("/", this.fileType)
      this.$http.post(url, form,
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
