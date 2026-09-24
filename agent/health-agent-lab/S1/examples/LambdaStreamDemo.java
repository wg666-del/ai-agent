import java.util.*;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 * LambdaStreamDemo · Lambda / 函数式接口 / Stream API / Optional
 *
 * 运行方式（JDK 11+ 单文件直接运行）：
 *   java LambdaStreamDemo.java
 *
 * 对应教程：d2.md 第 10、11、12 章。
 */
public class LambdaStreamDemo {

    /** 嵌套 record：用户数据 */
    record User(String name, int age, String city) { }

    public static void main(String[] args) {
        lambdaDemo();
        streamDemo();
        optionalDemo();
    }

    /** 1. Lambda 与函数式接口 */
    static void lambdaDemo() {
        System.out.println("== 1. Lambda ==");

        Runnable task = () -> System.out.println("  无参 Lambda 执行了");
        task.run();

        Function<Integer, Integer> doubleIt = x -> x * 2;              // 入参 -> 出参
        System.out.println("doubleIt(21) = " + doubleIt.apply(21));

        Predicate<Integer> isPositive = x -> x > 0;                    // 返回 boolean
        System.out.println("isPositive(-5) = " + isPositive.test(-5));

        Consumer<String> printer = s -> System.out.println("  " + s);  // 只消费
        printer.accept("Hello Lambda");

        // 方法引用：Lambda 的简写
        List.of("a", "b").forEach(System.out::println);
    }

    /** 2. Stream：像 JS 数组方法一样处理集合 */
    static void streamDemo() {
        System.out.println("\n== 2. Stream ==");

        List<User> users = List.of(
                new User("小明", 25, "杭州"),
                new User("小红", 17, "上海"),
                new User("老王", 40, "杭州"),
                new User("小李", 30, "北京"),
                new User("小张", 19, "上海"));

        // filter + map + collect：【TS 对照】users.filter(...).map(...)
        List<String> adultNames = users.stream()
                .filter(u -> u.age() >= 18)
                .map(User::name)
                .collect(Collectors.toList());
        System.out.println("成年人名字: " + adultNames);

        // 计数
        System.out.println("成年人数: " + users.stream().filter(u -> u.age() >= 18).count());

        // 排序：【TS 对照】[...users].sort((a, b) => a.age - b.age)
        List<User> sorted = users.stream()
                .sorted(Comparator.comparingInt(User::age))
                .collect(Collectors.toList());
        System.out.println("按年龄排序: " + sorted);

        // 分组（TS 里要手写 reduce，Java 内置）：按城市分组
        Map<String, List<User>> byCity = users.stream()
                .collect(Collectors.groupingBy(User::city));
        byCity.forEach((city, list) -> System.out.println("  " + city + " => " + list));

        // 判断与聚合：【TS 对照】some / every / reduce
        System.out.println("有未成年人吗: " + users.stream().anyMatch(u -> u.age() < 18));
        System.out.println("都成年了吗: " + users.stream().allMatch(u -> u.age() >= 18));
        System.out.println("年龄总和: " + users.stream().mapToInt(User::age).sum());
        System.out.println("平均年龄: " + users.stream().mapToInt(User::age).average().orElse(0));

        // 找最大：返回 Optional
        Optional<User> oldest = users.stream().max(Comparator.comparingInt(User::age));
        System.out.println("最年长的人: " + oldest.orElseThrow());
    }

    /** 3. Optional：优雅处理「可能为空」 */
    static void optionalDemo() {
        System.out.println("\n== 3. Optional ==");

        Map<String, Integer> stock = new HashMap<>();
        stock.put("苹果", 10);

        int apple = Optional.ofNullable(stock.get("苹果")).orElse(0);   // 存在 -> 10
        int melon = Optional.ofNullable(stock.get("西瓜")).orElse(0);   // 不存在 -> 0
        System.out.println("apple = " + apple + ", melon = " + melon);

        Optional.ofNullable(stock.get("苹果"))
                .map(n -> "苹果库存: " + n)
                .ifPresent(System.out::println);

        stock.clear();
        Optional.ofNullable(stock.get("苹果"))
                .map(n -> "苹果库存: " + n)
                .ifPresent(msg -> System.out.println("不会打印：" + msg));
        System.out.println("（库存被清空后，链式调用安全地什么都不做）");
    }
}
