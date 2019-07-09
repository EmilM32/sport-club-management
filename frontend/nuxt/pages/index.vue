<template>
  <v-container grid-list-md text-xs-center>
  <v-layout
    row
    wrap
  >
    <v-flex
      xs12
      sm4
    >
      <v-card
        :height="cardHeight">
        <v-card-title class="headline"></v-card-title>
        <v-card-text>
          
        </v-card-text>
        <v-card-actions>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-flex>
    <v-flex
      xs12
      sm4
    >
      <v-card
        :height="cardHeight">
        <v-card-title class="headline"></v-card-title>
        <v-card-text>
          
        </v-card-text>
        <v-card-actions>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-flex>
    <v-flex
      xs12
      sm4
    >
      <v-card
      :height="cardHeight">
        <v-card-title class="headline"></v-card-title>
        <v-card-text>
          
        </v-card-text>
        <v-card-actions>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-flex>
    <v-flex
      xs12
      sm4
    >
      <v-card
      :height="cardHeight">
        <v-card-title class="headline"></v-card-title>
        <v-card-text>
          
        </v-card-text>
        <v-card-actions>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-flex>
    <v-flex
      xs12
      sm4
    >
      <v-card
      :height="cardHeight">
        <v-card-title class="headline"></v-card-title>
        <v-card-text>
          
        </v-card-text>
        <v-card-actions>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-flex>
    <v-flex
      xs12
      sm4
    >
      <v-card
      :height="cardHeight">
        <v-card-title class="headline"></v-card-title>
        <v-card-text>
          
        </v-card-text>
        <v-card-actions>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
  </v-container>
</template>

<script>
import axios from "axios"
export default {
  components: {},
  layout (context) {
    return 'default'
  },
  // fetch () {
    
  // },
  // async asyncData ({ params }) {
  //   let { data } = await axios.get(`http://localhost:8000/get_data_fee/`)
  //   return { data }
  // },
  async fetch ({ store, params }) {
    await store.dispatch('GET_FEE');
  },
  data: () => ({
      imgWidth: 150,
      cardHeight: 200,
  }),
  methods: {

  },
  mounted() {
    // console.log(this.data)
  }
}
</script>
