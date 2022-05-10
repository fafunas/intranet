import Vue from 'vue'
import Vuex from 'vuex'

import news from './modules/news'
import notifications from './modules/notifications'
import dialog from './modules/dialog'
import user from './modules/user'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    news,
    notifications,
    dialog,
    user
  }
})
