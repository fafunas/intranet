<template>
  <v-app>
    <Navbar/>

    <v-main>
      <Login/>
      <router-view/>
    </v-main>
    <Footer/>
  </v-app>
</template>

<script>

import Navbar from "./components/Navbar.vue"
import Footer from "./components/Footer.vue"
import Login from "./components/Login.vue"

export default {
  name: 'App',
  components: {Navbar,Footer,Login}
  

 
};
</script>
