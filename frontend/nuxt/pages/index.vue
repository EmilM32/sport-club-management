<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm4>
        <v-card :height="cardHeight">
          <v-card-title class="headline"></v-card-title>
          <v-card-text></v-card-text>
          <v-card-actions>
            <v-spacer />
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex xs12 sm4>
        <v-card :height="cardHeight">
          <v-card-title class="headline"></v-card-title>
          <v-card-text></v-card-text>
          <v-card-actions>
            <v-spacer />
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex xs12 sm4>
        <v-card :height="cardHeight">
          <v-card-title class="headline"></v-card-title>
          <v-card-text></v-card-text>
          <v-card-actions>
            <v-spacer />
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex xs12 sm4>
        <v-card :height="cardHeight">
          <v-card-title class="headline"></v-card-title>
          <v-card-text></v-card-text>
          <v-card-actions>
            <v-spacer />
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex xs12 sm4>
        <v-card :height="cardHeight">
          <v-card-title class="headline"></v-card-title>
          <v-card-text></v-card-text>
          <v-card-actions>
            <v-spacer />
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex xs12 sm4>
        <v-card :height="cardHeight">
          <v-card-title class="headline"></v-card-title>
          <v-card-text></v-card-text>
          <v-card-actions>
            <v-spacer />
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  components: {},
  layout(context) {
    return "default";
  },
  // fetch () {

  // },
  // async asyncData ({ params }) {
  //   let { data } = await axios.get(`http://localhost:8000/get_data_fee/`)
  //   return { data }
  // },
  async fetch({ store, params }) {
    await store.dispatch("GET_FEE");
  },
  data: () => ({
    imgWidth: 150,
    cardHeight: 200
  }),
  methods: {
    mapTest() {
      const map = new Map();
      map.set(1, "test");
      map.set("1", "test2");
      map.set(true, "test3");

      // console.log('size', map.size)
      // console.log('map', map)
      // console.log('map.get(1)', map.get(true))

      const obiekt = {
        jeden: "test_1",
        dwa: "test_2"
      };

      map.set("obj", obiekt);
      // console.log('obiekt', map.get('obj'))
      // console.log('map', map)

      map.set(obiekt, "obj2");
      // console.log('obiekt2', map.get(obiekt))
      // console.log('map', map)

      // for (const el of map.keys()) {
      //   console.log(el)
      // }
      // map.forEach((key, value) => {
      //   console.log(`key: ${key}, value: ${value}`)
      // })
      const send = Object.fromEntries(map);
      axios
        .post("http://localhost:8000/get_map/", send)
        .then(response => {
          // console.log(response)
        })
        .catch(error => new Error(error));

      // class Rectangle {
      //   constructor(width, height) {
      //     this._width = width;
      //     this._height = height;
      //   }
      //   set width(width) {
      //     this._width = width;
      //   }
      //   get width() {
      //     return this._width;
      //   }
      //   set height(height) {
      //     this._height = height;
      //   }
      //   get height() {
      //     return this._height;
      //   }
      //   get area() {
      //     return this._width * this._height;
      //   }
      // }
      // var r = new Rectangle(50, 20);
      // console.log(r.area === 1000);
      // console.log(r.height);
      // r.height = 7;
      // console.log(r.height);
      // console.log(r);
    }
  },
  mounted () {
    this.mapTest();
    // console.log(this.data)
  }
};
</script>
