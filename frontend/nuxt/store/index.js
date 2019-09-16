import axios from "axios"
export const state = () => ({
  feeData: [],
  personalData: {}
})
export const actions = {
  async GET_FEE ({ commit }) {
    const { data } = await axios.get('http://localhost:8000/get_data_fee/')
    commit('SET_FEE', data)
  },
}
export const mutations = {
  SET_FEE (state, data) {
    state.feeData = data
  },
  PERSONAL_DATA (state, data) {
    state.personalData = data
  },
}