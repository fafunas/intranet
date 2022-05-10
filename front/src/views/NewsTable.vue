<template>
  <v-main class="pa-2">
        <NewsTable />
    
  </v-main>
</template>

<script>
import NewsTable from "../components/news/NewsTable.vue";

export default {
  components: { NewsTable },

  methods:{
    showDialog(){
      this.$store.dispatch("dialog/SET_DIALOG")
      
    }}

};
</script>

<style lang="scss" scoped>
</style>