import streamlit as st
import random
import matplotlib.pyplot as plt
from time import perf_counter

def insertion_sort(arr):
    swaps = 0
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
            comparisons += 1
        arr[j + 1] = key
        comparisons += 1
    return swaps, comparisons

def selection_sort(arr):
    swaps = 0
    comparisons = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return swaps, comparisons

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def test_sorting_algorithm(sort_function, input_array):
    start_time = perf_counter()
    swaps, comparisons = sort_function(input_array.copy())
    end_time = perf_counter()
    execution_time = end_time - start_time
    return swaps, comparisons, execution_time

def main():
    st.title("Sorting Algorithm Comparison")

    input_option = st.radio("Choose input option:", ("Generate Random Array", "Enter Manual Array"))

    if input_option == "Generate Random Array":
        input_size = st.number_input("Enter the size of the array to be sorted:", min_value=1, step=1)
        input_array = generate_random_array(input_size)
    else:
        input_string = st.text_input("Enter the elements of the array separated by spaces:")
        input_array = list(map(int, input_string.split()))

    if st.button("Sort"):
        st.write("\nSelected Array:")
        st.write(input_array)

        insertion_swaps, insertion_comparisons, insertion_time = test_sorting_algorithm(insertion_sort, input_array.copy())
        selection_swaps, selection_comparisons, selection_time = test_sorting_algorithm(selection_sort, input_array.copy())

        st.write("\nInsertion Sort:")
        st.write(f"Time taken: {insertion_time:.6f} seconds")
        st.write(f"Number of swaps: {insertion_swaps}")
        st.write(f"Number of comparisons: {insertion_comparisons}")

        st.write("\nSelection Sort:")
        st.write(f"Time taken: {selection_time:.6f} seconds")
        st.write(f"Number of swaps: {selection_swaps}")
        st.write(f"Number of comparisons: {selection_comparisons}")

        # Plotting
        labels = ['Insertion Sort', 'Selection Sort']
        times = [insertion_time, selection_time]
        swaps = [insertion_swaps, selection_swaps]
        comparisons = [insertion_comparisons, selection_comparisons]

        fig, axs = plt.subplots(1, 3, figsize=(15, 5))

        axs[0].bar(labels, times, color=['skyblue', 'salmon'])
        axs[0].set_ylabel('Time (seconds)')
        axs[0].set_title('Time Taken')

        axs[1].bar(labels, swaps, color=['lightgreen', 'lightcoral'])
        axs[1].set_ylabel('Number of Swaps')
        axs[1].set_title('Swaps')

        axs[2].bar(labels, comparisons, color=['lightblue', 'lightpink'])
        axs[2].set_ylabel('Number of Comparisons')
        axs[2].set_title('Comparisons')

        plt.tight_layout()
        st.pyplot(fig)

if __name__ == "__main__":
    main()
