export interface Task {
  id?: number;
  description: string;
  status: string;
  stimated: number;
  time: number;
}

export interface TaskPage {
  results: Array<Task>;
}