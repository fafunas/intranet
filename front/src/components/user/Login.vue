<template>
<v-main class="ma-4">
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      prepend-icon="mdi-account"
      v-model="name"
      :rules="nameRules"
      label="Usuario"
      required
    ></v-text-field>
    <v-text-field
    prepend-icon="mdi-lock"
    v-model="password"
    type="password"
    ></v-text-field>


    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="validate"
    >
      Login
    </v-btn>

  </v-form>
  </v-main>
</template>

<script>
  export default {
    data:()=>({
      valid:true,
      name:'',
      nameRules:[
        v=> !! v  || 'Usuario Obligatorio',
      ],
      password:''
    }),

    methods:{
      validate(){
        this.$refs.form.validate()
      }
    }

    
    
  }
</script>

<style lang="scss" scoped>

</style>