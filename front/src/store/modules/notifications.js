export default{

    namespaced: true,
    state:{
        drawer:null
    },

    mutations:{
        SHOW_DRAWER(state){
            state.drawer = "drawer"
        },
        FALSE_DRAWER(state){
            state.drawer =null
        }
    },

    actions:{
        SET_DRAWER:({commit})=>{
            commit("SHOW_DRAWER");
            setTimeout(function(){
                commit("FALSE_DRAWER");
            })
        },
        
    },


    getters:{
        drawer: state => state.drawer
    }







}