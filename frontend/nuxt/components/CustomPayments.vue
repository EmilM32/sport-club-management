<template>
  <v-container pa-0>
      <v-card 
        width="100%"
        elevation='0'
        color='grey lighten-5'>
           <v-layout row wrap align-center fill-height>

              <v-flex xs3 pl-4>
                <span>{{ $t('payments.custom') }}</span>
                <v-icon small @click='dialog = true'>visibility</v-icon>
              </v-flex>
              <v-spacer></v-spacer>
              <v-flex xs1>
                <v-text-field
                  v-model="value"
                  type="number"
                  class='nounderline'
                  label="PLN">
                </v-text-field>
              </v-flex>
              <v-flex xs5 pr-4>
                <v-select
                  v-model="monthsSelected"
                  :items="months"
                  class='nounderline'
                  chips
                  :label="$t('table.chooseMonth')"
                  multiple
                  flat
                ></v-select>
              </v-flex>
              <v-flex xs1>
                <v-btn
                  flat
                  icon
                  fab
                  color="grey darken-2"
                  @click='save'>
                  <v-icon>check_circle</v-icon>
                </v-btn>
              </v-flex>
           </v-layout>
      </v-card>
      <v-dialog
        v-model="dialog"
        width="500">
        <v-card>

          <v-card-text>
            <v-data-table
                :headers="tableHeaders"
                :items="tableItems"
                :rows-per-page-text="$t('table.rowsPerPage')"
              >
              <template v-slot:items="props">
                <td class='text-xs-center'>{{ props.item.month }}</td>
                <td class='text-xs-center'>{{ props.item.year }}</td>
                <td class='text-xs-center'>{{ props.item.value }}</td>
              </template>
            </v-data-table>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="grey"
              flat
              fab
              icon
              @click="dialog = false"
            >
              <v-icon>close</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
  </v-container>
</template>
<script>
import { mapMutations } from 'vuex'
import axios from "axios"
export default {
  props: [
    'selectedId'
  ],
  data () {
    return {
      months:['I','II','III','IV','V','VI','IX','X','XI','XII'],
      monthsSelected:[],
      value:'',
      dialog: false,
      tableHeaders: [
          { text: this.$t('table.month'), value: 'month', align: 'center' },
          { text: this.$t('table.year'), value: 'year', align: 'center' },
          { text: this.$t('table.paymentsValue'), value: 'value', align: 'center' },
      ],
      tableItems: [],
    }
  },
  methods: {
    ...mapMutations({
        setSnackSuccess: 'snackbarsuccess/setSnack',
        setSnackError: 'snackbarerror/setSnack',
      }),
    save() {
      const dataToSend = {
        'monthsSelected':this.monthsSelected,
        'year':new Date().getFullYear(),
        'value':this.value,
        'id': this.$props.selectedId
      }
      axios.post("http://localhost:8000/save_custom_payments/", dataToSend).then(response => {
          if (response.data.code == 1) {
            this.setSnackSuccess(this.$t('snackbar.success'))
          }
        }).catch(error => {
          this.setSnackError(this.$t('snackbar.error'))
          console.error('error',error)
        });
    },
    getCustomPayments() {
      axios.post("http://localhost:8000/get_data_payment_custom/", this.$props.selectedId).then(response => {
          this.tableItems = response.data.data
        }).catch(error => { console.error('error',error) });
    },
  },
  mounted() {
    this.getCustomPayments()
  }
}
</script>
<style>
.nounderline.v-text-field>.v-input__control>.v-input__slot:before {
    border-style: none;
}
.nounderline.v-text-field>.v-input__control>.v-input__slot:after {
    border-style: none;
}
.nounderline.v-select>.v-input__control>.v-input__slot:before {
    border-style: none;
}
.nounderline.v-select>.v-input__control>.v-input__slot:after {
    border-style: none;
}
</style>
