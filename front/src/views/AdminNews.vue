<template>
  <v-main class="pa-4">
    <div class="pa-2 btn"> <v-btn color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on">Agregar Noticia</v-btn></div>
    <div>
      <v-row>
        <v-col v-for="noti in news" :key="noti.id">
          <NewsList :news="noti" />
        </v-col>
      </v-row>
    </div>
  </v-main>
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
.btn{
  text-align: right;
}
</style>