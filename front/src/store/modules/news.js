import axios from "axios"

var NewsEndpoint= "http://127.0.0.1:8000/rest/v1/news/"

export default {
    namespaced: true,
    state: {
        news: [],
        token:[]
    },

    mutations: {
        //Get all the news
        NEWS(state, payload){
            state.news = payload
        },
        //Add new from adminNews
        ADDNEWS(state,payload){
            state.news.push(payload)
        }

    },

    actions: {
        getNews(context){
            axios.get(NewsEndpoint)
            .then((data)=>{
                context.commit("NEWS",data.data)
                console.log(data.data)
            })
          },

//Action to add new News          
        addNews(context,payload){
            axios.post(NewsEndpoint,payload)
            .then(()=>{
                context.commit("ADDNEWS",payload)
            })
            .catch((err)=> {console.error(`${err}`)})
        }

    },


    getters:{
        news: state => state.news
    }
}