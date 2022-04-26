<template>
<v-container>
  <div>
      <v-row>
          <v-col v-for="noti in news" :key="noti.id">
        <NewsList 
        :news="noti"/>
          </v-col>
      </v-row>
    
  </div>
  </v-container>
</template>

<script>
import NewsList from "../components/news/NewsList.vue";
import { mapGetters } from "vuex";
export default {
  components: { NewsList },
  computed: {
    ...mapGetters("news", ["news"]),
  },

  mounted() {
    this.$store.dispatch("news/getNews");

    // console.log()
  },
};
</script>

<style lang="scss" scoped>
</style>