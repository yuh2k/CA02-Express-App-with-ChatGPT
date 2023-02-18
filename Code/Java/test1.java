public class test1 {

    public static float fact(int n) {
        float res = 1;
        for (int i = 1; i < n + 1; i++) {
            res *= i;
        }
        return res;
    }
    public static void main(String[] args) {
        
        double prob = (4 * fact(13)) / (fact(8) * 52 * 51 * 50 * 49 * 48);
        
        System.out.println(String.format("%.8f", prob).toString());

    }
}
