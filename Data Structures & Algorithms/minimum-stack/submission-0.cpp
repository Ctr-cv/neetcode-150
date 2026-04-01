class MinStack {
public:
    stack<int> st1;
    stack<int> st2;
    MinStack() {}
    
    void push(int val) {
        st1.push(val);
        if (st2.empty() || val < st2.top()){
            st2.push(val);
        } else {
            st2.push(st2.top());
        }
    }
    
    void pop() {
        st1.pop();
        st2.pop();
    }
    
    int top() {
        return st1.top();
    }
    
    int getMin() {
        return st2.top();
    }
};
