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
      <div>{{news.shortDescription}}</div>

      
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="orange"
        text
      >
        <v-icon>mdi-note-edit
    </v-icon>
      </v-btn>

      <v-btn
        color="red"
        text
      >
        <v-icon>mdi-delete</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      {{news.update}}
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