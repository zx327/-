import streamlit as st
from PIL import Image

# --------------------------
# 1. 全局配置 + 自定义悬浮样式
# --------------------------
st.set_page_config(
    page_title="非遗数承·英歌舞教学",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 【关键】CSS：把Dify对话窗口固定在右下角，默认隐藏，点击卡通按钮显示/隐藏
st.markdown("""
<style>
.stApp {background-color: #fdf8f2;}
h1,h2,h3 {color: #c8102e; font-family: "Microsoft YaHei", sans-serif;}
div[data-testid="stVerticalBlock"] > div[style*="block"] {
    background: white; border-radius: 12px; padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.stButton>button {
    background: #c8102e; color: white; border-radius: 8px;
    border: none; width: 100%; height: 40px; font-weight: 500;
}
.stButton>button:hover {background: #a00c24;}
.css-1d391kg {background-color: #f8ece0;}

/* 悬浮对话窗口样式 */
#dify-chatbot-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 9999;
    display: none;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

/* 卡通按钮样式 */
#chatbot-toggle-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 10000;
    border: none;
    background: none;
    cursor: pointer;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
#chatbot-toggle-btn img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>
""", unsafe_allow_html=True)

# --------------------------
# 2. 全局变量&素材配置
# --------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "branch" not in st.session_state:
    st.session_state.branch = "new"
# 新增：控制对话窗口显示/隐藏
if "show_chatbot" not in st.session_state:
    st.session_state.show_chatbot = False

# 卡通角色图（替换成你的在线链接）
cartoon_img = {
    0: "https://raw.githubusercontent.com/zx327/-/main/0.png",
    1: "https://raw.githubusercontent.com/zx327/-/main/1.png",
    2: "https://raw.githubusercontent.com/zx327/-/main/2.png",
    3: "https://raw.githubusercontent.com/zx327/-/main/3.png",
    4: "https://raw.githubusercontent.com/zx327/-/main/4.png"
}
# 用你的卡通小人做悬浮按钮（用第0张图，也可以换其他）
chatbot_btn_img = cartoon_img[0]

teach_video = "https://raw.githubusercontent.com/zx327/-/main/vidio1.mp4"
step1_img = "https://raw.githubusercontent.com/zx327/-/main/01.png"
step2_img = "https://raw.githubusercontent.com/zx327/-/main/02.png"
step3_img = "https://raw.githubusercontent.com/zx327/-/main/03.png"
step4_img = "https://raw.githubusercontent.com/zx327/-/main/04.png"
standard_img = "https://raw.githubusercontent.com/zx327/-/main/4.png"
# 你的Dify聊天窗口链接（从Dify嵌入页面复制的iframe src）
dify_chat_url = "https://udify.app/chatbot/eC0lOS9PT3LZQiXP"

# --------------------------
# 3. 侧边栏：仅保留学习进度（干净无多余内容）
# --------------------------
with st.sidebar:
    st.title("📖 学习进度")
    step_name_list = ["诊学", "授法", "拆解", "陪练", "验成"]
    for idx, name in enumerate(step_name_list):
        if idx == st.session_state.step:
            st.markdown(f"### 🔴 {name}")
        else:
            st.markdown(f"⚪ {name}")
    st.markdown("---")
    st.image(cartoon_img[st.session_state.step], width="100%")
    st.caption("英歌舞小教头陪你学功夫～")

# --------------------------
# 4. 核心教学页面（所有use_column_width已替换为width="100%"）
# --------------------------

# 第0步：诊学（首页强提醒）
if st.session_state.step == 0:
    col_text, col_cartoon = st.columns([3, 1])
    with col_text:
        st.title("诊学·了解你的基础")
        st.subheader("你之前练过英歌舞内旋槌吗？")
        st.info(" 全程有国家级传承人认证的AI教学助教陪伴，点击右下角卡通小人，随时提问、动作纠错！")
        if st.button("没练过，从头学完整体系"):
            st.session_state.branch = "new"
            st.session_state.step = 1
        if st.button("练过，直接进入动作陪练"):
            st.session_state.branch = "experienced"
            st.session_state.step = 3
    with col_cartoon:
        st.image(cartoon_img[0], width="100%")
        st.caption("英歌舞小教头陪你从零学起～")
    st.caption("有问题，可以点击右下角卡通小人，打开与AI对话沟通哦")

# 第1步：授法
elif st.session_state.step == 1 and st.session_state.branch == "new":
    col_text, col_cartoon = st.columns([3, 1])
    with col_text:
        st.title("授法·观看大师示范")
        st.markdown("### 观察要点")
        st.info("握槌：掐而不紧、松而不滑 \n发力：手腕为轴，手臂固定 \n棒身：全程与地面平行")
        st.video(teach_video)
        st.markdown("### 动作口诀")
        st.success("握槌虚活不僵硬，手肘收紧槌水平；\n发力只在手腕处，旋转还原姿态正。")
        st.caption("💬 国家级非遗传承人陈来发：手腕是轴，手臂是架，只转手不甩臂，内旋才标准。")
        if st.button("看完了，进入拆解学习"):
            st.session_state.step = 2
    with col_cartoon:
        st.image(cartoon_img[1], width="100%")
        st.caption("跟着大师的动作，记住核心要点哦～")
    st.caption("有问题，可以点击右下角卡通小人，打开与AI对话沟通哦")

# 第2步：拆解
elif st.session_state.step == 2 and st.session_state.branch == "new":
    st.title("拆解·四步分解学习")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("第1步 预备握槌")
        st.image(step1_img, width="100%")
    with col2:
        st.subheader("第2步 内旋启动")
        st.image(step2_img, width="100%")
    with col3:
        st.subheader("第3步 水平定位")
        st.image(step3_img, width="100%")
    with col4:
        st.subheader("第4步 还原定型")
        st.image(step4_img, width="100%")
    if st.button("分步都学会了，进入陪练对比环节"):
        st.session_state.step = 3
    st.caption("有问题，可以点击右下角卡通小人，打开与AI对话沟通哦")

# 第3步：陪练
elif st.session_state.step == 3:
    st.title("陪练·左右对比纠错")
    col_standard, col_user, col_cartoon = st.columns([2, 2, 1])
    with col_standard:
        st.subheader("标准动作参考")
        st.image(standard_img, width="100%")
    with col_user:
        st.subheader("你的动作定格")
        user_img = st.file_uploader("上传你的动作照片", type=["png", "jpg", "jpeg"])
        if user_img:
            st.image(user_img, width="100%")
    with col_cartoon:
        st.image(cartoon_img[3], width="100%")
    st.markdown("---")
    st.markdown("### 跟练节奏口令")
    st.code("准备！1——握槌稳桩；2——手腕内旋；3——水平控槌；4——还原定型！")
    with st.expander("常见错误", expanded=True):
        st.write("1. 握槌过紧/过松 → 调整手指力度")
        st.write("2. 手肘外撇、棒身倾斜 → 手肘内收")
        st.write("3. 用手臂发力而非手腕 → 放松大臂")
        st.write("4. 还原不到位 → 手腕完整复位")
    if st.button("完成对比，进入验收"):
        st.session_state.step = 4
    st.caption("有问题，可以点击右下角卡通小人，打开与AI对话沟通哦")

# 第4步：验成
elif st.session_state.step == 4:
    col_text, col_cartoon = st.columns([3, 1])
    with col_text:
        st.title("恭喜完成英歌舞基础内旋槌学习！")
        check1 = st.checkbox("掌握内旋槌完整4步动作流程")
        check2 = st.checkbox("学会手腕为核心的正确发力技巧")
        check3 = st.checkbox("建立棒身平衡感，全程保持水平")
        check4 = st.checkbox("能独立完成标准4拍连贯动作")
        if check1 and check2 and check3 and check4:
            st.success("全部掌握！你已经解锁英歌舞内旋槌基本功！")
            st.balloons()
        if st.button("重新开始学习"):
            st.session_state.step = 0
            st.session_state.branch = "new"
    with col_cartoon:
        st.image(cartoon_img[4], width="100%")
    st.caption("有问题，可以点击右下角卡通小人，打开与AI对话沟通哦")

# --------------------------
# 🔥 【核心】卡通悬浮按钮 + Dify对话窗口
# --------------------------
# 1. 卡通按钮（点击切换显示/隐藏）
if st.button(" ", key="chatbot_toggle"):
    st.session_state.show_chatbot = not st.session_state.show_chatbot

# 2. 用CSS把按钮的文字替换成卡通图片（视觉效果）
st.markdown(f"""
<button id="chatbot-toggle-btn" onclick="document.querySelector('[key=chatbot_toggle]').click()">
    <img src="{chatbot_btn_img}" alt="AI助教">
</button>
""", unsafe_allow_html=True)

# 3. 对话窗口（根据状态显示/隐藏）
display = "block" if st.session_state.show_chatbot else "none"
st.components.v1.iframe(
    dify_chat_url,
    width=380,
    height=650,
    scrolling=True
)
# 把iframe固定在右下角
st.markdown(f"""
<style>
iframe {{
    position: fixed;
    bottom: 100px;
    right: 20px;
    z-index: 9999;
    border-radius: 12px;
    display: {display};
}}
</style>
""", unsafe_allow_html=True)