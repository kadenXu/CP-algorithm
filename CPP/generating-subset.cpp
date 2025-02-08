//generaing subset by bit sequences
for (int b = 0; b < (1<<n); b++) {
	vector<int> subset;
	for (int i = 0; i < n; i++) {
		if (b&(1<<i)) subset.push_back(i);
	}
	cout << "{ "; // printing
	for (auto j: subset) cout << j << " ";
	cout << "}\n"; // printing
}	
  
  
  // generating subset recursively
  vector<ll> subset;
  void generate (ll n, ll k) {
    if (n == k) {
      // proccesing the subset
    }
    generate(n, k+1);
    subset.push_back(k);
    generate(n, k+1);
    subset.pop_back();
  }
