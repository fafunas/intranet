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
                  <v-text-field
                    v-model="editNews.image"
                    label="File input"
                    filled
                    prepend-icon="mdi-camera"
                  ></v-text-field>
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
            <v-btn color="blue darken-1" text @click="dialog = false">
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
      }
  },

  mounted() {
    this.$store.dispatch("news/getNews");

    console.log("news");
  },
};
</script>

<style lang="sass" scoped>
</style>