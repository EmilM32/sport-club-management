<template>
  <v-app>
      <v-layout justify-center style="flex: 0;"  mb-4>
        <v-flex xs5>
            <v-text-field
              v-model="search"
              append-icon="search"
              single-line
              autofocus
              solo
              class='rounded'
              hide-details
            ></v-text-field>
        </v-flex>
      </v-layout>
      <v-card>
          <div>
            <v-data-table
              :headers="headers"
              :items="list"
              :search="search"
              :rows-per-page-text="$t('table.rowsPerPage')"
            >

              <template v-slot:items="props">
                <td @click="props.expanded = !props.expanded">
                  <span>{{props.item.first_name}}</span>
                </td>
                <td @click="props.expanded = !props.expanded">
                  <span>{{props.item.last_name}}</span>
                </td>
                <td class="pt-4 text-xs-center">
                  <v-checkbox 
                    v-model="props.item.september"
                    color="grey darken-2"
                  ></v-checkbox>
                </td>
                <td class="pt-4 text-xs-center">
                  <v-checkbox 
                    v-model="props.item.october"
                    color="grey darken-2"
                  ></v-checkbox>
                </td>
                <td class="pt-4 text-xs-center">
                  <v-checkbox 
                    v-model="props.item.november"
                    color="grey darken-2"
                  ></v-checkbox>
                </td>
                <td class="pt-4 text-xs-center">
                  <v-checkbox 
                    v-model="props.item.december"
                    color="grey darken-2"
                  ></v-checkbox>
                </td>
                <td class="pt-4 text-xs-center">
                  <v-checkbox 
                    v-model="props.item.january"
                    color="grey darken-2"
                  ></v-checkbox>
                </td>
                <td class="pt-4 text-xs-center">
                  <v-checkbox 
                    v-model="props.item.february"
                    color="grey darken-2"
                  ></v-checkbox>
                </td>
                <td class="pt-4 text-xs-center">
                  <v-checkbox 
                    v-model="props.item.march"
                    color="grey darken-2"
                  ></v-checkbox>
                </td>
                <td class="pt-4 text-xs-center">
                  <v-checkbox 
                    v-model="props.item.april"
                    color="grey darken-2"
                  ></v-checkbox>
                </td>
                <td class="pt-4 text-xs-center">
                  <v-checkbox 
                    v-model="props.item.may"
                    color="grey darken-2"
                  ></v-checkbox>
                </td>
                <td class="pt-4 text-xs-center">
                  <v-checkbox 
                    v-model="props.item.june"
                    color="grey darken-2"
                  ></v-checkbox>
                </td>
              </template>
              <template v-slot:expand="props">
              <CustomPayments :selectedId="props.item.id"/>
            </template>
            </v-data-table>
            <v-card-actions>
            <v-btn color="blue darken-1" fab large flat @click="saveToDb"><v-icon>save</v-icon></v-btn>
            <v-spacer></v-spacer>
            </v-card-actions>
          </div>
    </v-card>
  </v-app>
</template>
<script>
import CustomPayments from './../components/CustomPayments.vue'
import { mapMutations } from 'vuex'
import axios from "axios"
  export default {
    components: {
      CustomPayments
    },
    async fetch ({ store, params }) {
      // TODO
    },
    data () {
      return {
        headers: [
          { text: this.$t('table.name'), value: 'first_name' },
          { text: this.$t('table.surname'), value: 'last_name' },
          { text: 'IX', value: 'september' },
          { text: 'X', value: 'october' },
          { text: 'XI', value: 'november' },
          { text: 'XII', value: 'december' },
          { text: 'I', value: 'january' },
          { text: 'II', value: 'february' },
          { text: 'III', value: 'march' },
          { text: 'IV', value: 'april' },
          { text: 'V', value: 'may' },
          { text: 'VI', value: 'june' },
        ],
        list: [],
        expand: true,
        search: '',
        selectedId:'',
      }
    },
    methods: {
      saveToDb() {
        axios.post("http://localhost:8000/send_data_fee/", this.list).then(response => {
          if (response.data.code == 0) {
            this.setSnackSuccess(this.$t('snackbar.success'))
          }
        }).catch(error => {
          this.setSnackError(this.$t('snackbar.error'))
          console.error('error',error)
        });
      },
      getData() {
        axios.get("http://localhost:8000/get_data_fee/").then(response => {
          this.list = response.data.data
        }).catch(error => {
          console.error('error',error)
        });
      },
      fillPayments() {
        axios.post("http://localhost:8000/fill_payments/").then(response => {
          if (response.data.code == 0) {
            this.setSnackInfo(this.$t('snackbar.fillPayments'))
          }
        }).catch(error => {
          console.error('error',error)
        });
      },
      ...mapMutations({
        setSnackSuccess: 'snackbarsuccess/setSnack',
        setSnackError: 'snackbarerror/setSnack',
        setSnackInfo: 'snackbarinfo/setSnack',
      }),
    },
    mounted() {
      this.getData()
    },
  }
</script>
<style>
.rounded.v-input .v-input__slot {
  border-radius: 100px!important;
}
</style>
