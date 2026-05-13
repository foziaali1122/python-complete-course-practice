import streamlit as st
from datetime import date
from main import TodoApp
from utils import load_css
import pandas as pd
import plotly.express as px

#page config
st.set_page_config(
    page_title = "Smart Todo App",
    layout="centered"
)


load_css()

app = TodoApp()

#sidebar 
st.sidebar.title(" Smart Todo App")

#theme = st.sidebar.toggle("🌙 Dark Mode", value=True)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Task",
        "View Tasks"
    ]
)


# Dashboard
# =====================================

if menu == "Dashboard":

    st.title("📊 Dashboard")
    total_tasks = len(app.tasks)
    completed_tasks = len(
        [task for task in app.tasks if task["completed"]]
    )

    pending_tasks = total_tasks - completed_tasks
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Tasks", total_tasks)
    col2.metric("Completed", completed_tasks)
    col3.metric("Pending", pending_tasks)

    # =========================
    # Chart Data
    # =========================

    chart_data = pd.DataFrame({

        "Status": ["Completed", "Pending"],

        "Tasks": [completed_tasks, pending_tasks]
    })


    # =========================
    # Pie Chart
    # =========================

    pie_chart = px.pie(

        chart_data,

        names="Status",

        values="Tasks",

        title="Task Status Overview",

        hole=0.4,

        color_discrete_sequence=[
            "#80a1ed",
            "#ff4d97"
        ]
    )

    pie_chart.update_layout(

        title_font_size=24,

        font=dict(
            size=16,
            color="white"
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )


    # =========================
    # Line Chart
    # =========================

    line_data = pd.DataFrame({

        "Date": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri"
        ],

        "Completed": [1, 3, 2, 5, completed_tasks]
    })


    line_chart = px.line(

        line_data,

        x="Date",

        y="Completed",

        markers=True,

        title="Weekly Productivity"
    )

    line_chart.update_layout(

        title_font_size=24,

        font=dict(
            size=16,
            color="white"
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)"
    )

    line_chart.update_traces(

        line=dict(
            width=4,
            color="#06b6d4"
        ),

        marker=dict(
            size=10,
            color="#ed80c5"
        )
    )

    st.plotly_chart(
        line_chart,
        use_container_width=True
    )

 # Add Task
elif menu == "Add Task":

    st.title("➕ Add Task")
    title = st.text_input("Task Title")
    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )

    due_date = st.date_input(
        "Due Date",
        date.today()
    )

    if st.button("Add Task"):

        if title:
            app.add_task(title, priority, due_date)
            st.success("Task Added Successfully")
            st.rerun()

        else:
            st.warning("Please enter task title")

# View Tasks
elif menu == "View Tasks":

    st.title(" Your Tasks")

    search = st.text_input("🔍 Search Tasks")
    
    filter_option = st.selectbox(
    "Filter Tasks",
    ["All", "Completed", "Pending"]
)
    filtered_tasks = []

    for task in app.tasks:

        if search.lower() in task["title"].lower():

            if filter_option == "Completed" and not task["completed"]:
                continue

            if filter_option == "Pending" and task["completed"]:
                continue

            filtered_tasks.append(task)


    for index, task in enumerate(filtered_tasks):
        priority_class = task["priority"].lower()

        st.markdown(
            f"""
            <div class='task-card {priority_class}-border'>

            <div class='title {"completed" if task["completed"] else "pending"}'>
            {task['title']}
            </div>

            <div class='task-info'>
            <b>Priority:</b>

            <span class='{priority_class}'>
            {task['priority']}
            </span>
            </div>

            <div class='task-info'>
            <b>Due Date:</b>
            {task['due_date']}
            </div>

            <div class='task-info'>
            <b>Status:</b>
            {'✅ Completed' if task['completed'] else '⏳ Pending'}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        col1, col2, col3 = st.columns(3)
   
       #complete button
        if not task["completed"]:

            if col1.button(
                f"Complete {index}",
                key=f"complete_{index}"
            ):

                app.complete_task(index)
                st.rerun()

         # Delete Button
        if col2.button(
            f"Delete {index}",
            key=f"delete_{index}"
        ):

            app.delete_task(index)
            st.rerun()

        #Edit button
        new_title = col3.text_input(
            f"Edit Task {index}",
            key=f"edit_input_{index}"
        )

        if col3.button(
            f"Update {index}",
            key=f"update_{index}"
        ):

            if new_title:
                app.edit_task(index, new_title)
                st.success("Task Updated")
                st.rerun()
