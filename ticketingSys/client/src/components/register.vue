<!-- Register.vue -->
<template>
    <div>
        <hi>Register</hi>
        <br>
        <input
          type="username"
          name="username"
          v-model="username"
          placeholder="Username"/>
          <br>
        <input
          type="password"
          name="password"
          v-model="password"
          placeholder="Password"/>
        <br>
        <div class="error" v-html="error" />
        <br>
        <button @click="register">Register</button>
    </div>
  </template>
  
  <script>
  import authenticationService from '../services/authentication'
  export default {
    data() {
      return {
        username: '',
        password: '',
        error: null
      }
    },
    methods: {
      async register () {
        try {
          await authenticationService.register({
            username: this.username,
            password: this.password
          })
        } catch (error) {
          console.log(error)
          this.error = error.response.data.error
        }
      }
    }
  }
  </script>
  <style scoped>
  .error {
    color: red
  }

</style>