Chào bạn, đây là hướng dẫn giải chi tiết cho các bài tập trong đề cương ôn tập Trí tuệ nhân tạo (ngoại trừ phần bài tập dự án như bạn yêu cầu).

---

# PHẦN 1: TÁC TỬ (AGENTS)

### Câu 1:
**a. Mô tả PEAS cho tác tử giảng dạy chơi bóng đá:**
*   **Performance (Hiệu suất):** Số trận thắng của đội bóng, sự cải thiện kỹ năng của cầu thủ, điểm số trong bài kiểm tra chiến thuật, sự an toàn của người chơi.
*   **Environment (Môi trường):** Sân bóng, cầu thủ, bóng, khung thành, đối thủ (nếu có trong bài tập mô phỏng).
*   **Actuators (Bộ thực thi):** Màn hình hiển thị (để vẽ sơ đồ), loa/giọng nói (để chỉ đạo), còi, hoặc cánh tay robot (nếu là robot thực tế chỉ trỏ).
*   **Sensors (Cảm biến):** Camera (theo dõi vị trí cầu thủ/bóng), Microphone (nghe phản hồi), bàn phím/chuột (nhận input từ người học).

**b. Ví dụ về môi trường: Tác tử đơn lẻ, quan sát đầy đủ, không xác định (stochastic) và rời rạc.**
*   **Ví dụ:** Một chương trình chơi trò chơi **Backgammon (Cờ thỏ cáo)** (nhưng chơi ở chế độ luyện tập một mình hoặc giải thế cờ đổ xí ngầu). Hoặc đơn giản hơn là **Robot phân loại rác trên băng chuyền** (nếu coi việc gió thổi hoặc vị trí rác rơi là ngẫu nhiên).
*   **Giải thích:**
    *   *Tác tử đơn lẻ:* Nó tự chơi hoặc tự ra quyết định, không có đối thủ trực tiếp chống lại nước đi của nó (trong ví dụ luyện tập).
    *   *Quan sát đầy đủ:* Nhìn thấy toàn bộ bàn cờ/băng chuyền.
    *   *Không xác định (Stochastic):* Do có yếu tố gieo xí ngầu (Backgammon) hoặc rác bị trượt/gió thổi (Robot), kết quả hành động không chắc chắn 100% dẫn đến trạng thái tiếp theo.
    *   *Rời rạc:* Các ô trên bàn cờ, các mặt xí ngầu, hoặc các loại rác là đếm được rõ ràng.

### Câu 2:
**a. Mô tả PEAS cho tác tử phục vụ nhà hàng:**
*   **P:** Tiền tip, sự hài lòng của khách, tốc độ phục vụ, độ chính xác của món ăn, không làm rơi vỡ.
*   **E:** Bàn ghế, nhà bếp, khách hàng, đầu bếp, sàn nhà.
*   **A:** Bánh xe/chân di chuyển, tay cầm khay, giọng nói/màn hình giao tiếp.
*   **S:** Camera (nhận diện khách/đường đi), cảm biến va chạm, micro (nghe gọi món).

**b. Ví dụ về môi trường: Đa tác tử, quan sát đầy đủ, xác định, rời rạc.**
*   **Ví dụ:** Trò chơi **Cờ vua (Chess)**.
*   **Giải thích:**
    *   *Đa tác tử:* Có 2 người chơi (Trắng và Đen) cạnh tranh nhau.
    *   *Quan sát đầy đủ:* Cả hai đều nhìn thấy toàn bộ bàn cờ và vị trí các quân.
    *   *Xác định:* Không có xí ngầu hay yếu tố may mắn, di chuyển quân xe là quân xe sẽ đến đúng ô đó.
    *   *Rời rạc:* Các ô cờ và các lượt đi là hữu hạn, rõ ràng.

### Câu 3 (Tác tử chơi cờ tính giờ):
**a. PEAS:**
*   **P:** Thắng trận, không hết giờ, số quân ăn được.
*   **E:** Bàn cờ, quân cờ, đồng hồ, đối thủ.
*   **A:** Cơ chế di chuyển quân cờ (hoặc màn hình hiển thị nước đi), nút bấm đồng hồ.
*   **S:** Camera/Cảm biến bàn cờ (nhận biết vị trí quân), cảm biến thời gian.
**b. Đặc điểm môi trường:** Xác định (Deterministic), Quan sát đầy đủ (Fully Observable), Đa tác tử (Multi-agent), Rời rạc (Discrete), Chiến lược (Strategic).

### Câu 4 (Tác tử nhận dạng vân tay):
**a. PEAS:**
*   **P:** Tỷ lệ nhận diện đúng (True Positive), tỷ lệ từ chối sai (False Rejection), tốc độ mở khóa.
*   **E:** Ngón tay người dùng, bề mặt cảm biến, bụi bẩn/mồ hôi.
*   **A:** Chốt khóa điện tử (mở/đóng), đèn báo/màn hình.
*   **S:** Cảm biến vân tay (quang học/siêu âm/điện dung).
**b. Đặc điểm môi trường:** Tác tử đơn lẻ, Quan sát một phần (chỉ thấy bề mặt da, không thấy bên trong hoặc ngón tay bị bẩn), Không xác định (Stochastic - do nhiễu), Rời rạc (Kết quả là Mở hoặc Không mở), Theo chuỗi (Episodic - lần mở này không ảnh hưởng lần sau).

---

# PHẦN 2: TÌM KIẾM (SEARCH)

### Câu 1: Bản đồ Romania (Lugoj -> Bucharest)

**a. Các thuật toán tìm kiếm không thông tin (Blind Search):**
*Lưu ý: Thứ tự duyệt phụ thuộc vào cách cài đặt (thường là Alphabet).*

1.  **BFS (Theo chiều rộng):**
    *   Duyệt theo từng lớp.
    *   Lugoj -> Mehadia, Timisoara -> Drobeta, Arad -> Craiova, Sibiu -> ... -> Bucharest.
    *   Đường đi tìm được (ít số cạnh nhất): **Lugoj -> Mehadia -> Drobeta -> Craiova -> Pitesti -> Bucharest.**
2.  **UCS (Chi phí cực tiểu):**
    *   Luôn mở rộng nút có chi phí $g(n)$ thấp nhất.
    *   Lugoj(0) -> Mehadia(70), Timisoara(111).
    *   Chọn Mehadia(70) -> Drobeta(70+75=145).
    *   Chọn Timisoara(111) -> Arad(111+118=229).
    *   Chọn Drobeta(145) -> Craiova(145+120=265).
    *   ... -> Pitesti -> Bucharest.
    *   Đường đi: **Lugoj -> Mehadia -> Drobeta -> Craiova -> Pitesti -> Bucharest** (Tổng chi phí: 504).
3.  **DFS (Theo chiều sâu):**
    *   Đi sâu hết mức có thể. Giả sử ưu tiên bảng chữ cái.
    *   Lugoj -> Mehadia -> Drobeta -> Craiova -> Pitesti -> Bucharest. (May mắn trúng ngay đích).
4.  **IDS (Sâu dần):**
    *   Lặp lại DFS với độ sâu giới hạn $d=0, 1, 2, \dots$ cho đến khi thấy đích.

**b. Tìm kiếm Heuristic (GBFS và A*):**
*Heuristic $h(n)$ theo bảng trong đề.*

1.  **GBFS (Tham lam):** Luôn chọn nút có $h(n)$ nhỏ nhất.
    *   Tại Lugoj ($h=244$): Kề {Mehadia(241), Timisoara(329)}. -> Chọn **Mehadia**.
    *   Tại Mehadia ($h=241$): Kề {Drobeta(242), Lugoj}. -> Chọn **Drobeta**.
    *   Tại Drobeta ($h=242$): Kề {Craiova(160), ...}. -> Chọn **Craiova**.
    *   Tại Craiova ($h=160$): Kề {Pitesti(10), ...}. -> Chọn **Pitesti**.
    *   Tại Pitesti ($h=10$): Kề {Bucharest(0), ...}. -> Chọn **Bucharest**.
    *   Kết quả: **Lugoj -> Mehadia -> Drobeta -> Craiova -> Pitesti -> Bucharest**.

2.  **A* (A-Star):** Chọn nút có $f(n) = g(n) + h(n)$ nhỏ nhất.
    *   *Open:* {Lugoj: $0+244=244$}
    *   *Pop Lugoj.* Thêm: {Mehadia: $70+241=311$, Timisoara: $111+329=440$}.
    *   *Pop Mehadia (311).* Thêm Drobeta: $70+75+242 = 387$.
    *   *Open:* {Drobeta: 387, Timisoara: 440}.
    *   *Pop Drobeta (387).* Thêm Craiova: $145+120+160 = 425$.
    *   *Open:* {Craiova: 425, Timisoara: 440}.
    *   *Pop Craiova (425).* Thêm Pitesti: $265+138+10 = 413$, Rimnicu: $265+146+193 = 604$.
    *   *Open:* {Pitesti: 413, Timisoara: 440, Rimnicu: 604}.
    *   *Pop Pitesti (413).* Thêm Bucharest: $403+101+0 = 504$.
    *   *Open:* {Timisoara: 440, Bucharest: 504, ...}.
    *   *Pop Timisoara (440).* (Do A* phải duyệt hết các khả năng nhỏ hơn đích). Thêm Arad: $111+118+366 = 595$.
    *   *Open:* {Bucharest: 504, Arad: 595, Rimnicu: 604}.
    *   *Pop Bucharest (504).* -> **ĐÍCH**.
    *   Đường đi: **Lugoj -> Mehadia -> Drobeta -> Craiova -> Pitesti -> Bucharest**. Chi phí: 504.

### Câu 2: Cây trò chơi (Minimax)
**a. Minimax:**
*   Điền giá trị từ dưới lên:
    *   Tầng sát lá (Min):
        *   Nút con trái: min(6, 4, 2) = 2.
        *   Nút con giữa: min(5, 3, 6) = 3.
        *   Nút con phải: min(10, 1) = 1.
        *   Nhóm tiếp theo: min(1, 2) = 1.
        *   Nhóm cuối: min(1, 9, 8, 20) = 1.
    *   Tầng trên (Max):
        *   Nhánh trái: max(2, 3) = 3.
        *   Nhánh giữa: max(1) = 1. (Lưu ý hình vẽ hơi rối, giả sử các ô vuông là Max).
        *   Nhánh phải: max(1, 1) = 1.
    *   Gốc (Max): max(3, 1, 1) = **3**.
*   Cạnh Max chọn: Đi theo nhánh dẫn đến giá trị 3 (Nhánh trái ngoài cùng).

**b. Alpha-Beta Pruning:**
*   Cần thực hiện duyệt từ trái sang phải và duy trì $\alpha$ (giá trị tốt nhất cho Max), $\beta$ (tốt nhất cho Min).
*   Cắt tỉa xảy ra khi giá trị tìm được tồi tệ hơn giá trị đã có ở nhánh khác (với Min là $\le \alpha$, với Max là $\ge \beta$).
*   Ví dụ cụ thể trên hình (mô phỏng): Khi Max đã tìm được giá trị 3 ở nhánh đầu. Sang nhánh 2, Min tìm thấy số 1. Vì $1 < 3$ nên Min sẽ không bao giờ chọn nhánh này để cho Max hưởng lợi lớn hơn 3 (nếu có các con khác lớn hơn 1). Max cũng không quan tâm vì Max đã có 3 chắc chắn rồi. -> **Cắt các nhánh còn lại của nút Min đó.**

### Câu 5 (Trang 6): Negamax & Branch and Bound
*(Dựa vào hình cây màu xanh/vàng)*
1.  **Điểm số Negamax:** Tính từ dưới lên, đảo dấu mỗi lần lên tầng.
    *   Nút lá (xanh): -18, -23, 30, 70, 90, 60, 40, -10, 80, 40, 15, 10, 25, 8, 20, 55.
    *   Nút cha (vàng - Min trong Minimax chuẩn, nhưng Negamax sẽ lấy max(-con)):
        *   Nút vàng 1: max(-(-18), -(-23)) = max(18, 23) = 23.
        *   Nút vàng 2: max(-30, -70) = -30.
        *   ... (tương tự cho các nút khác).
2.  **Cắt tỉa Alpha-Beta:**
    *   Duyệt trái sang phải. Nếu tìm thấy giá trị khiến đối thủ không bao giờ đi vào nhánh đó thì cắt.
3.  **Branch and Bound (Mã giả):**
    *   Đoạn mã giả thực hiện tìm kiếm sâu dần với một cận `bound`.
    *   Dòng 9: `if score >= bound return score;` đây chính là điều kiện cắt nhánh (tương tự Beta cut-off).

---

# PHẦN 3: SUY DIỄN (LOGIC)

### Câu 1:
**a. Dạng chuẩn CNF:**
Quy tắc: $A \Rightarrow B \equiv \neg A \lor B$.
1.  $\neg y \lor \neg z \lor e$
2.  $(\neg x \lor \neg z \lor f) \land (\neg x \lor \neg z \lor g)$
3.  $(\neg t \lor x \lor y) \land (\neg z \lor x \lor y)$
4.  $\neg y \lor \neg t \lor g$
5.  $\neg z \lor \neg e \lor g$
6.  $\neg t \lor e$
7.  $\neg y \lor \neg t \lor h$
8.  $z$
9.  $t$

**b. Chứng minh $(g \land e)$:**
Tức là cần chứng minh $g$ đúng VÀ $e$ đúng.
*   **Chứng minh $e$:**
    *   Có (9) $t$ và (6) $t \Rightarrow e$.
    *   Hợp giải: $e$. (Đã chứng minh được vế 1).
*   **Chứng minh $g$:**
    *   Có (8) $z$ và (1) $y \land z \Rightarrow e$ (không trực tiếp giúp tìm g).
    *   Có (5) $z \land e \Rightarrow g$.
    *   Ta đã có $z$ (từ 8) và $e$ (vừa chứng minh trên).
    *   Suy ra $g$.
*   Kết luận: $g \land e$ là Đúng.

### Câu 2: Chứng minh $a \land e$
Giả thiết:
1. $a$
2. $b$
3. $a \to c$
4. $c \to d$
5. $(b \land d) \to e$

**Quá trình suy diễn:**
1.  Từ (1) và (3), dùng Modus Ponens: Có $a$ và $a \to c$ $\Rightarrow$ **$c$**.
2.  Từ kết quả $c$ và (4), dùng Modus Ponens: Có $c$ và $c \to d$ $\Rightarrow$ **$d$**.
3.  Từ (2) có $b$, và vừa chứng minh được $d$, dùng quy tắc Hội (Conjunction): $\Rightarrow$ **$b \land d$**.
4.  Từ kết quả $(b \land d)$ và (5), dùng Modus Ponens: $\Rightarrow$ **$e$**.
5.  Từ (1) có $a$, và vừa chứng minh $e$, dùng quy tắc Hội: $\Rightarrow$ **$a \land e$**. (ĐPCM).

### Câu 3: Logic món cá
Ký hiệu: A (Amy đỏ), B (Betty đỏ), C (Cindy đỏ), D (Diane đỏ).
(Nếu không đỏ thì là Xanh $\neg A$).
Các phát biểu:
1.  Trong {A, C, D} có đúng 2 người đỏ: $(A \land C \land \neg D) \lor (A \land \neg C \land D) \lor (\neg A \land C \land D)$.
2.  Betty và Cindy khác màu: $B \Leftrightarrow \neg C$.
3.  Cindy và Diane khác màu: $C \Leftrightarrow \neg D$.
4.  Amy và Betty khác màu: $A \Leftrightarrow \neg B$.

**Giải:**
*   Từ (3): C và D khác màu -> Một đỏ, một xanh.
*   Từ (1): Trong {A, C, D} có 2 đỏ. Vì {C, D} luôn có đúng 1 đỏ (do khác màu), nên bắt buộc **A phải là Đỏ**.
*   Có $A = True$ (Đỏ).
*   Từ (4): A và B khác màu -> $B = False$ (Xanh).
*   Từ (2): B và C khác màu -> $C = True$ (Đỏ).
*   Từ (3): C và D khác màu -> $C=True \Rightarrow D=False$ (Xanh).
*   **Kết quả:** Amy: Đỏ, Betty: Xanh, Cindy: Đỏ, Diane: Xanh.
*   **c. Chứng minh Betty gọi món cá xanh:** Đã suy diễn ra $B = False$ (Xanh) ở trên. Phương pháp hợp giải sẽ dùng phủ định kết luận (Giả sử Betty Đỏ) và chứng minh mâu thuẫn.

---

# PHẦN 4: HỌC MÁY (MACHINE LEARNING)

### Câu 1: Linear Regression
Dữ liệu: X = [5, 10, 15, 20, 25], Y = [2, 3, 6, 4, 8]. $n=5$.

**a. Tính $b_0, b_1$:**
Lập bảng tính:
*   $\sum X = 75 \Rightarrow \bar{X} = 15$
*   $\sum Y = 23 \Rightarrow \bar{Y} = 4.6$
*   $\sum XY = (5\cdot2 + 10\cdot3 + 15\cdot6 + 20\cdot4 + 25\cdot8) = 10 + 30 + 90 + 80 + 200 = 410$
*   $\sum X^2 = (25 + 100 + 225 + 400 + 625) = 1375$

Công thức:
$$b_1 = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2} = \frac{5(410) - 75(23)}{5(1375) - 75^2}$$
$$b_1 = \frac{2050 - 1725}{6875 - 5625} = \frac{325}{1250} = 0.26$$

$$b_0 = \bar{Y} - b_1\bar{X} = 4.6 - 0.26(15) = 4.6 - 3.9 = 0.7$$

Phương trình: **$Y = 0.7 + 0.26X$**

**b. Dự đoán tại X = 17:**
$$Y = 0.7 + 0.26(17) = 0.7 + 4.42 = 5.12$$
Vậy điểm dự đoán là **5.12**.

**c. Tính MSE (Mean Squared Error):**
Tính lỗi bình phương cho từng điểm dữ liệu so với $Y_{pred}$.
*   $X=5, Y=2, \hat{Y}=2.0 \rightarrow (0)^2 = 0$
*   $X=10, Y=3, \hat{Y}=3.3 \rightarrow (-0.3)^2 = 0.09$
*   $X=15, Y=6, \hat{Y}=4.6 \rightarrow (1.4)^2 = 1.96$
*   $X=20, Y=4, \hat{Y}=5.9 \rightarrow (-1.9)^2 = 3.61$
*   $X=25, Y=8, \hat{Y}=7.2 \rightarrow (0.8)^2 = 0.64$
$$MSE = \frac{0 + 0.09 + 1.96 + 3.61 + 0.64}{5} = \frac{6.3}{5} = 1.26$$

### Câu 2: k-NN
Dữ liệu: $A(1,1,-1)$; $B(1,7,+1)$; $C(3,3,+1)$; $D(5,4,-1)$; $E(2,5,-1)$.
Điểm cần phân loại: $U(3,6)$.

**a. k=3, khoảng cách Manhattan:** $d = |x_1-x_2| + |y_1-y_2|$
*   $d(U, A) = |3-1| + |6-1| = 2 + 5 = 7$
*   $d(U, B) = |3-1| + |6-7| = 2 + 1 = 3$ (Lớp +1)
*   $d(U, C) = |3-3| + |6-3| = 0 + 3 = 3$ (Lớp +1)
*   $d(U, D) = |3-5| + |6-4| = 2 + 2 = 4$
*   $d(U, E) = |3-2| + |6-5| = 1 + 1 = 2$ (Lớp -1)

Sắp xếp khoảng cách tăng dần: E(2), B(3), C(3), D(4), A(7).
Lấy k=3 láng giềng gần nhất: E(-1), B(+1), C(+1).
Đa số: 2 dấu (+) và 1 dấu (-).
**Kết quả:** Phân loại lớp **+1**.

**b. Trọng số:**
Khi thay đổi trọng số (ví dụ nhân cả 2 trục tọa độ với 0.5), khoảng cách Euclit tương đối giữa các điểm vẫn giữ nguyên tỷ lệ (chỉ bị co lại). Do đó thứ tự gần nhất không đổi. Kết quả **không đổi**.

### Câu 3: Naive Bayes
Dữ liệu có 10 dòng.
*   $P(Y=True) = 5/10 = 0.5$
*   $P(Y=False) = 5/10 = 0.5$

Đầu vào: **A=1, B=0, C=1**.

**Tính cho lớp True:**
Xét 5 dòng có Y=True (Dòng 1, 2, 5, 6, 10).
*   $P(A=1|True)$: Có 2 dòng (2, 10) có A=1 $\rightarrow 2/5 = 0.4$.
*   $P(B=0|True)$: Có 1 dòng (6) có B=0 $\rightarrow 1/5 = 0.2$.
*   $P(C=1|True)$: Có 3 dòng (1, 5, 10) có C=1 $\rightarrow 3/5 = 0.6$.
Likelihood(True) = $0.5 \times 0.4 \times 0.2 \times 0.6 = \mathbf{0.024}$.

**Tính cho lớp False:**
Xét 5 dòng có Y=False (Dòng 3, 4, 7, 8, 9).
*   $P(A=1|False)$: Có 3 dòng (3, 4, 8) có A=1 $\rightarrow 3/5 = 0.6$.
*   $P(B=0|False)$: Có 3 dòng (3, 8, 9) có B=0 $\rightarrow 3/5 = 0.6$.
*   $P(C=1|False)$: Có 4 dòng (3, 4, 7, 8) có C=1 $\rightarrow 4/5 = 0.8$.
Likelihood(False) = $0.5 \times 0.6 \times 0.6 \times 0.8 = \mathbf{0.144}$.

**Kết luận:**
Vì $0.144 > 0.024$, nhãn dự đoán cho dữ liệu đầu vào là **False**.
