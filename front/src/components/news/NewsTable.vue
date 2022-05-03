<template>
<v-container>
    
        <v-data-table
        :headers = "tableHeaders"
        :items = "news"
        class="elevation-1">
        <template v-slot:item.image="{item}">
            <v-img
      class="white--text align-end"
      width=120px
      height="80px"
      :src="item.image"
    >
            </v-img>
        </template>
        <template v-slot:item.action="{item}">
             <v-icon medium color="#30E587" class="mr-2" @click="cargarEdicion(item)">
                mdi-pencil
              </v-icon>
              <v-icon medium color="red" @click="deleteItem(item.id)"> mdi-delete </v-icon>
        </template>
            
        </v-data-table>
    </v-container>  
</template>

<script>
import {mapGetters} from 'vuex'
    export default {
        data() {
            return {
                tableHeaders: [
                    {text : 'Fecha Publicacion' , value: 'update'},
                    {text : 'Imagen', value : 'image'},
                    {text : 'Titulo', value: 'name'},
                    {text : 'Descripcion' , value: 'shortDescription'},
                    {text: 'Accion', value: 'action'}
                ]
            }
        },

        computed:{
            ...mapGetters("news",["news"])
        },

        mounted() {
    this.$store.dispatch("news/getNews");

    console.log("news")
  },



        
    }
</script>

<style lang="sass" scoped>

</style>