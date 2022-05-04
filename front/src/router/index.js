import Vue from 'vue'
import VueRouter from 'vue-router'
//import Carrousel from '../views/Carrousel.vue'
import Carrousel from '../components/Carrousel.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Carrousel
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  // {
  //   path:'/admin',
  //   name:'admin',
  //   component: () => import('../views/AdminNews.vue')
  // },
  {
    path:'/newspanel',
    name:'News',
    component: () => import('../views/NewsTable.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
