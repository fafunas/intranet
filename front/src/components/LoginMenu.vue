<template>
     <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
      right
      color="grey lighten-5"
    >
      <div v-if="login">
          <UserPanel/>
          </div>  
      <div v-else>
          <Login/>
      </div>
    </v-navigation-drawer>
</template>

<script>

import {mapState} from 'vuex'
import Login from './user/Login.vue'
import UserPanel from './user/UserPanel.vue'

    export default {
        data() {
            return {
                login: localStorage.getItem("token")
            }
        },
        components:{Login,UserPanel},

    computed:{
        ...mapState('notifications',['drawer'])
    }
    }
</script>

<style lang="scss" scoped>

</style>