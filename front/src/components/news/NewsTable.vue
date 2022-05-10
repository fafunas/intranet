<template>
  <v-container>
           
    <!-- Dialog para carga de noticia nueva y edicion de la misma -->
    <v-row justify="center">
      <v-dialog v-model="dialog" max-width="600px">
          <template v-slot:activator="{on,attrs}">
              <v-btn
              color="primary"
              dark
              class="ma-4"
              v-bind="attrs"
              v-on="on"
              >Nueva Noticia</v-btn>
          </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">Nueva Noticia</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editNews.name"
                    label="Titulo*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-textarea
                    v-model="editNews.description"
                    label="Descripcion*"
                    type="Descripcion"
                    required
                  ></v-textarea>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-file-input
                    :src="editNews.image"
                    label="File input"
                    accept="image/*"
                    prepend-icon="mdi-camera"
                    @change="upload"
                    required
                  ></v-file-input>
                  <input type="file" @change="upload">
                </v-col>
              </v-row>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="dialog = false">
              Cerrar
            </v-btn>
            <v-btn color="blue darken-1" text @click="saveItem()">
              Guardar
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
    <v-data-table :headers="tableHeaders" :items="news" class="elevation-1">
      <template v-slot:item.image="{ item }">
        <v-img
          class="white--text align-end"
          width="120px"
          height="80px"
          :src="item.image"
        >
        </v-img>
      </template>
      <template v-slot:item.action="{ item }">
        <v-icon
          medium
          color="#30E587"
          class="mr-2"
          @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon medium color="red" @click="deleteItem(item.id)">
          mdi-delete
        </v-icon>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import axios from 'axios'
import { mapGetters } from "vuex";
export default {
  data: () => ({
    dialog: false,
    editNews: {
      name: "",
      description: "",
      image: "",
    },
    //Headers for the table
    tableHeaders: [
      { text: "Fecha Publicacion", value: "update" },
      { text: "Imagen", value: "image" },
      { text: "Titulo", value: "name" },
      { text: "Descripcion", value: "shortDescription" },
      { text: "Accion", value: "action" },
    ],
  }),

  computed: {
    ...mapGetters("news", ["news"]),
  },
  methods:{
      editItem(id){
          this.editNews.name = id.name.toString()
          this.editNews.description = id.description.toString()
          this.editNews.image = id.image.toString()
          this.dialog = true
          console.log(id.id)
      },

      saveItem(){
        
      
    
      },

      upload(event){
        const formData = new FormData();
        let image = event.target.files[0]
        formData.append('name', this.editNews.name)
        formData.append('description', this.editNews.description)
       formData.append('image', image)
        let config = {
      header : {
       'Content-Type' : 'multipart/form-data'
     }
    }
      axios.post("http://127.0.0.1:8000/rest/v1/news/", formData, config)
    
    
    
    // for (var pair of formData.entries()) {
    //     console.log(pair[0] + ", " + pair[1]);
    //   }
      console.log(event)
      }
  },

  mounted() {
    this.$store.dispatch("news/getNews");

  //  console.log("news");
  },
};
</script>

<style lang="sass" scoped>
</style>