<template>
  <v-carousel cycle height="500" hide-delimiter-background show-arrows-on-hover>
    <v-carousel-item v-for="item in news" :key="item.id"  :src="item.image">
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="text-h2">
          {{item.name}}
          </div>
        </v-row>
     
    </v-carousel-item>
  </v-carousel>
</template>

<script>
import { mapGetters } from "vuex";

export default {

  computed: {
    ...mapGetters('news',['news']),
  },

  mounted() {
    this.$store.dispatch("news/getNews");

    // console.log()
  },
};
</script>

<style lang="scss" scoped>
.text-h2{
  color: white;
 
}

img{
  opacity: 0.5;
}

</style>