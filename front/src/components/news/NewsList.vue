<template>
  <v-card
    class="mx-auto"
    max-width="300"
  >
    <v-img
      class="white--text align-end"
      height="150px"
      :src="news.image"
    >
      
    </v-img>

    <v-card-subtitle class="pb-0">
      {{news.name}}
    </v-card-subtitle>

    <v-card-text class="text--primary">
      <div>{{news.description}}</div>

      
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="orange"
        text
      >
        Modificar
      </v-btn>

      <v-btn
        color="orange"
        text
      >
        Eliminar
      </v-btn>
      <v-spacer></v-spacer>
      {{news.created}}
    </v-card-actions>
  </v-card>
</template>

<script>
export default{
    props:{
        news:[]
    }
}
</script>

<style lang="scss" scoped>
</style>