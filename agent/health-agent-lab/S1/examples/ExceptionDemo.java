/**
 * ExceptionDemo · 异常处理：try/catch/finally、受检异常、自定义异常、try-with-resources
 *
 * 运行方式（JDK 11+ 单文件直接运行）：
 *   java ExceptionDemo.java
 *
 * 对应教程：d2.md 第 9 章。
 */
public class ExceptionDemo {

    public static void main(String[] args) {
        basicTryCatch();
        multiCatch();
        checkedException();
        tryWithResources();
    }

    /** 1. 基本 try-catch-finally */
    static void basicTryCatch() {
        System.out.println("== 1. try / catch / finally ==");
        try {
            int r = divide(10, 0);   // 这里会抛异常
            System.out.println("不会执行到这: " + r);
        } catch (ArithmeticException e) {   // 捕获具体类型的异常
            System.out.println("捕获异常：" + e.getMessage());
        } finally {
            System.out.println("finally：无论是否异常都会执行（常用于释放资源）");
        }
    }

    /** 2. 多个 catch：从具体到宽泛 */
    static void multiCatch() {
        System.out.println("\n== 2. 多个 catch ==");
        try {
            String s = null;
            s.length();                      // 抛出 NullPointerException
        } catch (NullPointerException e) {   // 子类异常写在前面
            System.out.println("空指针异常被捕获");
        } catch (RuntimeException e) {       // 父类异常写后面（兜底）
            System.out.println("其他运行时异常被捕获");
        }
    }

    /** 3. 受检异常（checked）：编译期就强制处理 —— Java 特色，TS 没有 */
    static void checkedException() {
        System.out.println("\n== 3. 受检异常 ==");
        // register("", 18);   // <- 不处理会编译报错，必须 try-catch 或向上 throws

        try {
            register("", 18);
        } catch (InvalidInputException e) {
            System.out.println("注册失败：" + e.getMessage());
        }

        try {
            register("小明", 25);
        } catch (InvalidInputException e) {
            System.out.println("不会走到这：" + e.getMessage());
        }
    }

    /** 4. try-with-resources：自动关闭资源 */
    static void tryWithResources() {
        System.out.println("\n== 4. try-with-resources ==");
        try (FakeConnection conn = new FakeConnection()) {
            conn.query();
        } // 离开 try 块自动调用 conn.close()
        System.out.println("（连接已被自动关闭）");
    }

    // ---------- 工具方法 ----------

    static int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("除数不能为 0");   // 抛出异常
        }
        return a / b;
    }

    static void register(String name, int age) throws InvalidInputException {
        if (name == null || name.isEmpty()) {
            throw new InvalidInputException("用户名不能为空");   // 抛出受检异常
        }
        System.out.println("注册成功：" + name);
    }

    /** 自定义「受检异常」：继承 Exception */
    static class InvalidInputException extends Exception {
        public InvalidInputException(String message) {
            super(message);
        }
    }

    /** 模拟一个「需要关闭」的资源（实现 AutoCloseable） */
    static class FakeConnection implements AutoCloseable {
        FakeConnection() { System.out.println("  [资源] 打开连接"); }

        void query() { System.out.println("  [资源] 执行查询..."); }

        @Override
        public void close() { System.out.println("  [资源] 关闭连接"); }
    }
}
