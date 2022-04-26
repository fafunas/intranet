<template>
    <div>
            <v-app-bar
      app
      color="grey lighten-5"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Moviport"
          class="shrink mr-2"
          contain
          src='../assets/logo.png'
          transition="scale-transition"
          width="150"
        />

      </div>

      <v-spacer></v-spacer>

      <v-btn
        text
        color="primary"
        @click.stop= showDrawer()
      >
        <span class="mr-2">Login</span>
        <v-icon left> mdi-account </v-icon>
      </v-btn>
     
    </v-app-bar>
    </div>
</template>

<script>
    export default {

      methods:{
        showDrawer(){
          this.$store.dispatch("notifications/SET_DRAWER")
          console.log("Hola papa")
        }
      }
    
  }
</script>

<style lang="scss" scoped>

</style>