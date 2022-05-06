<template>
     <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
      right
      color="grey lighten-5"
    >
      <Login/>
    </v-navigation-drawer>
</template>

<script>

import {mapState} from 'vuex'
import Login from './user/Login.vue'

    export default {
        components:{Login},

    computed:{
        ...mapState('notifications',['drawer'])
    }
    }
</script>

<style lang="scss" scoped>

</style>