<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-img
      class="white--text align-end"
      height="200px"
     
    >
      <v-card-title></v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">
      {{news.created}}
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
        color="orange"
        text
      >
        More...
      </v-btn>
      
    </v-card-actions>
  </v-card>
</template>

<script>
    export default {
        props:{
            news:[]
        },

        mounted(){
            console.log(this.news)
        }
    }

</script>

<style lang="scss" scoped>

</style>