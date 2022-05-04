<template>
  <v-app>
    <Navbar/>

    <v-main>
      <LoginMenu/>
      <router-view/>
    </v-main>
    <Footer/>
  </v-app>
</template>

<script>

import Navbar from "./components/Navbar.vue"
import Footer from "./components/Footer.vue"
import LoginMenu from "./components/LoginMenu.vue"

export default {
  name: 'App',
  components: {Navbar,Footer,LoginMenu}
  

 
};
</script>
