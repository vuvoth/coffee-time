import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class BloomFilter {
    int m, k;
    HashMap<Integer, Integer> B = new HashMap<>();

    public BloomFilter(int _m, int _k) {
        this.m = _m;
        this.k = _k;
    }

    public BloomFilter(int _m, int _k, List<Integer> S) {
        this.m = _m;
        this.k = _k;
        for (Integer s : S) {
            add(s);
        }
    }

    /**
     * hash function i-th
     * 
     * @param value
     * @param i
     * @return hash of value use hash function i-th
     */
    int hash(int value, int i) {
        return (value + i) % this.m;
    }

    public void add(int s) {
        for (int i = 0; i < this.k; ++i)
            B.put(hash(s, i), 1);
    }

    /**
     * Check s is inside set of number BloomFilter
     * 
     * @param s
     * @return boolean
     */
    public boolean query(int s) {
        for (int i = 0; i < this.k; ++i) {
            if (B.get(hash(s, i)) == null) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        List<Integer> S = Arrays.asList(1, 6, 7, 8, 3, 7, 9);

        BloomFilter bloomFilter = new BloomFilter(100, 3, S);
        for (int s : S) {
            System.out.printf("Number %d exist in set number = %b\n", s, bloomFilter.query(s));
        }

        System.out.println("-----------------------------------------------");
        S = Arrays.asList(100, 3, 79, 8, 34, 7, 5);
        for (int s : S) {
            System.out.printf("Number %d exist in set number = %b\n", s, bloomFilter.query(s));
        }
    }
}