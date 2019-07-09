<template>
  <v-snackbar 
    v-model="show"
   :timeout="timeout"
   color='blue darken-1'>
    <span class='text-xs-center'>{{message}}</span>
    <v-btn flat fab icon @click.native="show = false"><v-icon color="white">close</v-icon></v-btn>
  </v-snackbar>
</template>

<script>
export default {
  data () {
    return {
      show: false,
      message: '',
      timeout: 3500,
    }
  },
  created: function () {
      this.$store.watch(state => state.snackbarinfo.snack, () => {
        const msg = this.$store.state.snackbarinfo.snack
        if (msg !== '') {
          this.show = true
          this.message = this.$store.state.snackbarinfo.snack
          this.$store.commit('snackbarinfo/setSnack', '')
        }
      })
  }
}
</script>