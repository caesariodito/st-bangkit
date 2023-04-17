# Structuring ML Projects

- Week 1
    
    Motivation
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled.png)
    
    Orthogonalization → Making one knob only control 1 ‘action’
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%201.png)
    
    example of ‘knobs’
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%202.png)
    
    Single Evaluation Number Metric → Lebih efisien untuk memilih algoritma
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%203.png)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%204.png)
    
    1. Optimizing: 1st priority → highest accuracy
    2. Satisficing: 2nd priority → running time ≤ 100ms
    
    Tujuan: mencari the ‘best one’
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%205.png)
    
    Dev/Test Distribution
    
    Dev and Test sets harus dateng dari sumber yang sama.
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%206.png)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%207.png)
    
    Size of Dev and Test set
    
    Old way
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%208.png)
    
    Modern
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%209.png)
    
    Test set: < 30% → sediain sebutuhnya
    
    Better ada Dev dan Test
    
    When to change Dev/Test sets or change the metrics?
    
    Example:
    
    Algo A better but contains p***-images → not recommended for user, not preferable
    
    Algo B less better but gud for user → choose algo B
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2010.png)
    
    Dev/test yang dipake harus kurleb sama kek yang bakal dipake si user
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2011.png)
    
    Ada 2 “knob” yang udah didapet
    
    - “adjusting the target” → define metric
    - “how well we shoot to the target” → ACC?
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2012.png)
    
    ML Performance → ga bisa ngelebihin “Bayes optimal error”
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2013.png)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2014.png)
    
    Avoidable bias
    
    Kalo gap dari human ke train error lebih tinggi dibanding train ke dev → search for avoidable bias techniques (train a bigger network)
    
    kebalikannya → search for variance reduction techniques (regularization, get more data, etc) 
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2015.png)
    
    Sama kek sebelumnya, bayes error ga beda jauh ama human level performance
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2016.png)
    
    Surpassing Human-level performance
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2017.png)
    
    ### Summary
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2018.png)
    
- Week 2
    
    Evaluasi manual terkait data yang missclassified, cari yang berpengaruh paling tinggi 
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2019.png)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2020.png)
    
    .
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2021.png)
    
    **COBA AJA DULU**
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2022.png)
    
    Split Case Data (mobile app target) to 50%,
    
    10k → 5k training, 2.5k dev, 2.5k test
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2023.png)
    
    Data Mismatch → berbeda dengan variance/overfitting, masalah baru
    
    → meningkatkan insights terkait apa yang salah pada bagian variance problem/overfitting
    
    → membuat set baru → training dev set
    
    → terjadi ketika train-dev ke dev error tinggi
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2024.png)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2025.png)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2026.png)
    
    Address Data Mismatch
    
    → bikin syntethic data juga bisa
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2027.png)
    
    Hati - hati overfitting pada data sintetis, perhatikan ‘space’ juga dari data sintetis tsb
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2028.png)
    
    Transfer Learning
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2029.png)
    
    When to use transfer learning
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2030.png)
    
    Multi-task learning → bedanya cuman dari output
    
    Kita mau ngedetect multiple object at the same time (ada mobil ga?? ada stop sign ga?? ada traffic ga??)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2031.png)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2032.png)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2033.png)
    
    Kalo tasknya mirip, itu gud (having shared lower-level features)
    
    End-to-end learning
    
    → Taking x input and map it to Y (tanpa ekstraksi fitur dsb)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2034.png)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2035.png)
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2036.png)
    
    - end-to-end ga selalu bagus karena ada case dimana kek yg face recognition
        - ada multiple orang di dalam 1 gambar (camera) → gimana cara nentuin orang yang mau di input?
        - maka dari itu di crop dulu, baru di recognize
    
    Pros and cons end-to-end DL
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2037.png)
    
    nek datane sitik, turu wae, rasah nggo end-to-end
    
    ![Untitled](Structuring%20ML%20Projects%20a696e15e366f43e0a76936d806e592cd/Untitled%2038.png)