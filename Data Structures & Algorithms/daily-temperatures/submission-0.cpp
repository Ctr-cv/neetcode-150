class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int warm = 0;
        stack<tuple<int, int>> st;
        vector<int> result(temperatures.size());
        for (int i = 0; i < temperatures.size(); i++){
            while (!st.empty() && get<0>(st.top()) < temperatures[i]){
                auto t = st.top();
                st.pop();
                result[get<1>(t)] = i - get<1>(t);
            }
            st.push(make_tuple(temperatures[i], i));
        }
        while (!st.empty()){
            auto t = st.top();
            st.pop();
            result[get<1>(t)] = 0;
        }
        return result;
    }
};
