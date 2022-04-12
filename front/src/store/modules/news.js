import axios from "axios"

export default {
    namespaced: true,
    state: {
        news: [],
        token:[]
    },

    mutations: {
        NEWS(state, payload){
            state.news = payload
        }

    },

    actions: {
        getNews(context){
            axios.get("http://127.0.0.1:8000/rest/v1/news/")
            .then((data)=>{
                context.commit("NEWS",data.data)
                console.log(data.data)
            })
          }

    },


    getters:{
        news: state => state.news
    }
}