import axios from 'axios'
export default{

    namespaced: true,
    state:{
        token:null,
        refreshtoken:null,
        isAuthenticated: false,
        user:[],
        endpoints:{
            obtainJWT : 'http://127.0.0.1:8000/api/token/',
            refreshJWT: 'http://127.0.0.1:8000/api/token/refresh/'
        }
    },

    mutations:{
        setToken(state,{access, refresh}){
            state.token = access
            state.refreshtoken= refresh
            state.isAuthenticated = true
            localStorage.setItem("token", JSON.stringify({access,refresh}))
            
        },

        removeToken(state){
            state.token=null
            state.refreshtoken= null
            state.isAuthenticated = false
            localStorage.removeItem('token')
        }
    },

    actions:{
        userLogin(context, credentials){
            return new Promise((resolve,reject)=>{
                axios.post('http://127.0.0.1:8000/api/token/',{
                    username: credentials.username,
                    password: credentials.password
                })
                .then(response=>{
                    context.commit("setToken",{access: response.data.access, refresh: response.data.refresh})
                    console.log(response)
                    resolve()
                })
                .catch(err=>{
                    reject(err)
                    console.log(err)
                })
            })
        }

    }

}